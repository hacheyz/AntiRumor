package cn.edu.hit.backend.pojo;

import lombok.Data;
import org.springframework.format.annotation.DateTimeFormat;

import java.time.LocalDate;

@Data
public class Rumor {
  private Integer id;
  private String rumor;
  private String truth;
  private String origin;
  @DateTimeFormat(pattern = "yyyy-MM-dd")
  private LocalDate published_date;
  private String url;

}
